// Fill out your copyright notice in the Description page of Project Settings.


#include "CharacterStatBase.h"

// Sets default values for this component's properties
UCharacterStatBase::UCharacterStatBase()
	:current(100.0f),max(100.0f),regenRate(0.1f),name(CharStatName::UNINITIALIZED)
{
	PrimaryComponentTick.bCanEverTick = true;
}

UCharacterStatBase::UCharacterStatBase( const float _current, const float _max, const float _regenRate, CharStatName _name)
	:current(_current),max(_max),regenRate(_regenRate),name(_name)
{
	PrimaryComponentTick.bCanEverTick = true;
}

// Called when the game starts
void UCharacterStatBase::BeginPlay()
{
	Super::BeginPlay();
	
}

float UCharacterStatBase::GetCurrent() const
{
	return this->current;
}
float UCharacterStatBase::GetMax() const
{
	return this->max;
}
float UCharacterStatBase::GetRegenRate() const
{
	return this->regenRate;
}
CharStatName UCharacterStatBase::GetName() const
{
	return this->name;
}

void UCharacterStatBase::SetCurrent(const float amount)
{
	check(amount > 0.0f);
	this->current = amount;
}

void UCharacterStatBase::SetMax(const float amount)
{
	check(amount > 0.0f);
	this->max = amount;
}

void UCharacterStatBase::SetRegenRate(const float amount)
{
	this->regenRate = amount;

}

void UCharacterStatBase::SetName(CharStatName _name)
{
	this->name = _name;
}


void UCharacterStatBase::PassiveTick()
{
	this->SetCurrent(this->GetCurrent() + this->GetRegenRate());
}

void UCharacterStatBase::Set(const float _current, const float _max, const float _regen, CharStatName _name)
{
	check(_current > 0.0f && _current <= _max);
	check(_max > 0.0f);
	check(_regen);
	this->current = _current;
	this->max = _max;
	this->regenRate = _regen;
	this->name = _name;
}