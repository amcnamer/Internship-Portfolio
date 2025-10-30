// Fill out your copyright notice in the Description page of Project Settings.


#include "ItemBase.h"

// Sets default values for this component's properties
UItemBase::UItemBase()
	:maxStackSize(0), currentStackSize(1), weight(0.0f), currencyCost(0.0f), itemName(TEXT("UNINITIALIZED")), 
	itemType(CharacterItemType::UNINITIALIZED), itemTier(CharacterItemTier::UNINITIALIZED)
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = false;

	// ...
}


// Called when the game starts
void UItemBase::BeginPlay()
{
	Super::BeginPlay();
	
}

float UItemBase::getWeight() const
{
	return this->weight;
}

float UItemBase::getCost() const
{
	return this->currencyCost;
}

int UItemBase::GetCurrentStackSize() const
{
	return this->currentStackSize;
}

int UItemBase::GetMaxStackSize() const
{
	return this->maxStackSize;
}

FString UItemBase::GetCharacterItemName() const
{
	return this->itemName;
}

CharacterItemTier UItemBase::GetCharacterItemTier() const
{
	return this->itemTier;
}

CharacterItemType UItemBase::GetCharacterItemType() const
{
	return itemType;
}

void UItemBase::AdjustStackSize(const int amount)
{
	this->currentStackSize += amount;
}

void UItemBase::Set(const int _maxStackSize, const int _currentStackSize, const float _weight, const float _currencyCost, FString _name, CharacterItemType _type, CharacterItemTier _tier)
{
	this->maxStackSize = _maxStackSize;
	this->currentStackSize = _currentStackSize;
	this->weight = -weight;
	this->currencyCost = _currencyCost;
	this->itemName = _name;
	this->itemType = _type;
	this->itemTier = _tier;
}


//// Called every frame
//void UItemBase::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
//{
//	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);
//
//	// ...
//}

