// Fill out your copyright notice in the Description page of Project Settings.


#include "CharacterStatComponent.h"

UCharacterStatComponent::UCharacterStatComponent()
{
	PrimaryComponentTick.bCanEverTick = true;
	Health = new UCharacterStatBase[]();
	Stamina = new UCharacterStatBase[]();
	Hunger = new UCharacterStatBase[]();
	Thirst = new UCharacterStatBase[]();
}


void UCharacterStatComponent::BeginPlay()
{
	Health->Set(100.0f, 100.0f, 0.1f, CharStatName::HEALTH);
	Stamina->Set(100.0f, 100.0f, 0.1f, CharStatName::STAMINA);
	Hunger->Set(100.0f, 100.0f, -0.05f, CharStatName::HUNGER);
	Thirst->Set(100.0f, 100.0f, -0.025f, CharStatName::THIRST);
	Super::BeginPlay();
}

// Called every frame
void UCharacterStatComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);
	if (TickType != ELevelTick::LEVELTICK_PauseTick)
	{
		this->PassiveAdjustment();
	}
}

float UCharacterStatComponent::GetPercent(CharStatName _name)
{
	check(_name != CharStatName::UNINITIALIZED) //assert
	switch (_name)
	{
	case(CharStatName::HEALTH):
		return((Health->GetCurrent() / Health->GetMax()) * 100);
	case(CharStatName::STAMINA):
		return((Stamina->GetCurrent() / Stamina->GetMax()) * 100);
	case(CharStatName::HUNGER):
		return((Hunger->GetCurrent() / Hunger->GetMax()) * 100);
	case(CharStatName::THIRST):
		return((Thirst->GetCurrent() / Thirst->GetMax()) * 100);
	default:
		return -1;
	}
}

int UCharacterStatComponent::Set(float _current, float _max, float _regenRate, CharStatName _name)
{
	check(_current > 0.0f && _current <= _max);
	check(_max > 0.0f);
	check(_regenRate);

	switch (_name)
	{
	case(CharStatName::HEALTH):
		Health->Set(_current, _max, _regenRate, _name);
		return 0;
	case(CharStatName::STAMINA):
		Stamina->Set(_current, _max, _regenRate, _name);
		return 0;
	case(CharStatName::HUNGER):
		Hunger->Set(_current, _max, _regenRate, _name);
		return 0;
	case(CharStatName::THIRST):
		Thirst->Set(_current, _max, _regenRate, _name);
		return 0;
	default:
		return -1;
	}
}

int UCharacterStatComponent::Adjust(float _amount, CharStatName _name)
{
	check(_amount);
	check(_name != CharStatName::UNINITIALIZED);

	switch (_name)
	{
	case(CharStatName::HEALTH):
		Health->SetCurrent(FMath::Clamp(Health->GetCurrent() + _amount, 0.0f, Health->GetMax()));
		return 0;
	case(CharStatName::STAMINA):
		Stamina->SetCurrent(FMath::Clamp(Stamina->GetCurrent() + _amount, 0.0f, Stamina->GetMax()));
		return 0;
	case(CharStatName::HUNGER):
		Hunger->SetCurrent(FMath::Clamp(Hunger->GetCurrent() + _amount, 0.0f, Hunger->GetMax()));
		return 0;
	case(CharStatName::THIRST):
		Thirst->SetCurrent(FMath::Clamp(Thirst->GetCurrent() + _amount, 0.0f, Thirst->GetMax()));
		return 0;
	default:
		return -1;
	}
}

void UCharacterStatComponent::PassiveAdjustment()
{
	Health->PassiveTick();
	Stamina->PassiveTick();
	Hunger->PassiveTick();
	Thirst->PassiveTick();
}
