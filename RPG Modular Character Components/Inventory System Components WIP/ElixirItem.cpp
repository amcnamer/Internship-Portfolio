// Fill out your copyright notice in the Description page of Project Settings.


#include "ElixirItem.h"
#include "CharacterStatComponent.h"

UElixirItem::UElixirItem()
	:statAdjustmentAmount(0.0f), elixirType(ElixirType::UNINITIALIZED)
{
}

void UElixirItem::Use(AActor* actor) const
{
	UCharacterStatComponent* StatComp = actor->FindComponentByClass<UCharacterStatComponent>();
	if (StatComp)
	{
		switch (this->elixirType)
		{
		case(ElixirType::HEALTH):
			StatComp->Adjust(this->statAdjustmentAmount,CharStatName::HEALTH);
			break;
		case(ElixirType::STAMINA):
			StatComp->Adjust(this->statAdjustmentAmount,CharStatName::STAMINA);
			break;
		default:
			break;
		}
	}
	//clean up for disposal
	StatComp = nullptr;
}

float UElixirItem::GetStatAdjustmentAmount() const
{
	return this->statAdjustmentAmount;
}

ElixirType UElixirItem::GetElixirType() const
{
	return this->elixirType;
}

void UElixirItem::Set(const int _maxStackSize, const int _currentStackSize, const float _weight, const float _currencyCost, 
	const float _statAdjustmentAmount, ElixirType _elixirType, FString _name, CharacterItemType _type, CharacterItemTier _tier)
{
	this->maxStackSize = _maxStackSize;
	this->currentStackSize = _currentStackSize;
	this->weight = -weight;
	this->currencyCost = _currencyCost;
	this->statAdjustmentAmount = _statAdjustmentAmount;
	this->elixirType = _elixirType;
	this->itemName = _name;
	this->itemType = _type;
	this->itemTier = _tier;
}
